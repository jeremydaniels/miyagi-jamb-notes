"""Clean text that goes into images and alt text: strip stray quotes, turn chemical formulas, ions, units and
caret/underscore notation into real subscripts and superscripts (CO_2 -> CO₂, m2 -> m², x^2 -> x², 10^-3 -> 10⁻³).

  from textfmt import fmt
"""
import re
SUB = str.maketrans("0123456789+-=()", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎")
SUP = str.maketrans("0123456789+-=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ")
ELS = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Ti V Cr Mn Fe Co Ni Cu Zn Br Ag Sn I Ba Au Hg Pb U Pu Ra".split()
_alt = "|".join(sorted(ELS, key=len, reverse=True))
FORMULA = re.compile(r"(?<![A-Za-z#_])((?:(?:%s)\d*|\((?:(?:%s)\d*)+\)\d*)+)(?![A-Za-z])" % (_alt, _alt))
DIATOMIC = {"H2", "O2", "N2", "O3", "Cl2", "Br2", "I2", "S8", "P4"}
UNIT_NEG = re.compile(r"(?<![A-Za-z0-9])((?:[kcdm]?m)|s|kg|g|N|J|K|Pa|W|mol|A)(-\d)(?![\d.,A-Za-z%])")      # s-1, kg m-3, N m-2
UNIT_POS = re.compile(r"(?<![A-Za-z0-9])([cdkm]m|(?<=\d )m|(?<=\d)m|(?<=/)s)([23])(?![\d.,A-Za-z%])")     # cm3, 5 m2, m/s2
NOT_FORMULA = re.compile(r"^(IC|AC|DC|AR|MR|MC|AP|AS|AD|AB|TC|TR|TP|VC|SR|LR|PS|CD|PC|MP|FC|SC|AVC|ATC|AFC)\d")
IONS = {"SO42-": "SO₄²⁻", "CO32-": "CO₃²⁻", "NO3-": "NO₃⁻", "HCO3-": "HCO₃⁻", "NH4+": "NH₄⁺", "H3O+": "H₃O⁺",
        "Fe2+": "Fe²⁺", "Fe3+": "Fe³⁺", "Cu2+": "Cu²⁺", "Zn2+": "Zn²⁺", "Ca2+": "Ca²⁺", "Mg2+": "Mg²⁺", "Al3+": "Al³⁺", "Pb2+": "Pb²⁺",
        "Ba2+": "Ba²⁺", "Ni2+": "Ni²⁺", "Mn2+": "Mn²⁺", "O2-": "O²⁻", "S2-": "S²⁻",
        "OH-": "OH⁻", "Rh+": "Rh⁺", "Rh-": "Rh⁻", "Na+": "Na⁺", "K+": "K⁺", "Ag+": "Ag⁺", "Li+": "Li⁺", "Cl-": "Cl⁻", "Br-": "Br⁻", "H+": "H⁺"}
ION_RE = re.compile(r"(?<![A-Za-z0-9])(%s)(?![A-Za-z0-9])" % "|".join(re.escape(k) for k in sorted(IONS, key=len, reverse=True)))


def _formula(m):
    t = m.group(1)
    if not re.search(r"[A-Za-z)]\d", t):
        return t
    if NOT_FORMULA.match(t):
        return t
    if re.fullmatch(r"[A-Z][a-z]?\d+", t) and t not in DIATOMIC:       # B12, F1, Q1, P2: vitamins and variables, not formulas
        return t
    return re.sub(r"\d+", lambda d: d.group(0).translate(SUB), t)


def strip_junk(text):
    """Stray quotes left by the placeholder parser around a label (not quotations inside real text)."""
    text = text.strip()
    if len(text) > 1 and text[0] == text[-1] and text[0] in "\"'`":
        text = text[1:-1].strip()
    elif text[:1] == '"' and text.count('"') == 1:
        text = text[1:].strip()
    return text


def fmt(text):
    if not text or "$" in text:
        return text
    text = re.sub(r"\^\{?([0-9+\-n]+)\}?", lambda m: m.group(1).translate(SUP), text)
    text = re.sub(r"_\{?([0-9+\-]+)\}?", lambda m: m.group(1).translate(SUB), text)
    text = ION_RE.sub(lambda m: IONS[m.group(1)], text)
    text = FORMULA.sub(_formula, text)
    text = UNIT_NEG.sub(lambda m: m.group(1) + m.group(2).translate(SUP), text)
    text = UNIT_POS.sub(lambda m: m.group(1) + m.group(2).translate(SUP), text)
    return text


if __name__ == "__main__":
    for t in ["CO_2 gas", "'Dilute HCl'", "KClO3 + MnO2 catalyst", "Fe2O3 and Ca(OH)2", "vitamin B12", "F1 hybrid", "m/s2 and cm3", "nitrogen gas (N2)",
              "y = x^2 - 4x + 3", "10^-3 kg m-3", "Rh+ baby", "Fe2+ ions", "Q1 and P2", "NH4Cl", "H2SO4", "2 cm cube", "1% copper", "CD4 cells", "Ozone (O3)", "s-1", "D1 + D2", "SO42- and OH-", "Cu2+ + 2e-", "P = IV, 5 m2", "A2 paper", "Vitamin K"]:
        print(repr(t), "->", fmt(t))
