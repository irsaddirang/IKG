"""
Shared constants + regex grammar for the manroland R700 IEC/UL circuit-diagram
knowledge base.

All geometry is in PDF points, origin top-left, y increasing downwards
(PyMuPDF convention).  Page size is 1190.551 x 841.890 pt (DIN A3 landscape).
"""

from __future__ import annotations

import re

# --------------------------------------------------------------------------
# Page geometry (measured; identical on all 1351 pages)
# --------------------------------------------------------------------------
PAGE_W = 1190.551
PAGE_H = 841.890

FRAME_X0 = 56.69
FRAME_X1 = 1176.38
FRAME_Y0 = 14.17
FRAME_Y1 = 827.72

# Title block band
TITLE_Y0 = 771.02
TITLE_Y1 = 827.72

# Drawing (circuit) area: everything above the title block, inside the frame
DRAW_Y0 = FRAME_Y0
DRAW_Y1 = 771.02

# Column letters A..H.  Centres measured from the margin letters.
COL_LETTERS = "ABCDEFGH"
COL_CENTRES = [128.9, 269.5, 411.2, 552.9, 694.6, 836.1, 978.1, 1120.1]
# Band boundaries: frame edge .. midpoints .. frame edge
COL_EDGES = [FRAME_X0]
for _i in range(len(COL_CENTRES) - 1):
    COL_EDGES.append(round((COL_CENTRES[_i] + COL_CENTRES[_i + 1]) / 2.0, 3))
COL_EDGES.append(FRAME_X1)

# Left-hand rotated legal notice strip: everything left of this x is boilerplate
NOTICE_X_MAX = 56.69


def column_of(x: float) -> str:
    """Map a page x coordinate to its DIN column letter A..H."""
    for i in range(len(COL_LETTERS)):
        if COL_EDGES[i] <= x < COL_EDGES[i + 1]:
            return COL_LETTERS[i]
    return COL_LETTERS[-1] if x >= COL_EDGES[-1] else COL_LETTERS[0]


def column_index(x: float) -> int:
    for i in range(len(COL_LETTERS)):
        if COL_EDGES[i] <= x < COL_EDGES[i + 1]:
            return i
    return 7 if x >= COL_EDGES[-1] else 0


# --------------------------------------------------------------------------
# Text normalisation
# --------------------------------------------------------------------------
def clean(s: str) -> str:
    """Normalise PDF text: soft hyphen / nbsp used as spacing by the CIM-TEAM
    exporter, plus stray tabs."""
    if s is None:
        return ""
    s = s.replace("\xad", " ")   # soft hyphen used as a word separator
    s = s.replace("\xa0", " ")   # no-break space
    s = s.replace("\t", " ")
    s = s.replace("\u200b", "")
    return re.sub(r" {2,}", " ", s).strip()


# --------------------------------------------------------------------------
# Label grammar
# --------------------------------------------------------------------------
# Cross reference: /13.G  -> sheet 13, column G   (optionally /13.G:pin )
RE_XREF = re.compile(r"^/(\d{1,3})\.([A-H])$")

# Current-path / line number (Rennzahl)
RE_PATHNO = re.compile(r"^#(\d{1,4})$")

# Device tag, e.g. +A497/2  -X3.A497  -X1.A368:1  A358/06  X602  +A497/1
RE_DEVTAG = re.compile(r"^([+\-]?)([A-Z]{1,2})(\d{2,4})(?:/(\d{1,2}))?(?:\.([A-Z]\d{2,4}))?(?::([0-9A-Za-z]{1,4}))?$")

# Bare device-location reference like "X26.A342:1" (no leading sign)
RE_DEVLOC = re.compile(r"^([A-Z]{1,2}\d{2,4})(?:\.([A-Z]\d{2,4}))?(?::([0-9A-Za-z]{1,4}))?$")

# Net / potential name, e.g. 24V 0V L24+ M24+ L24+/4 24V.X001:15
RE_NET = re.compile(r"^([A-Z]{0,2}\d{1,3}[A-Z]?(?:[+-]\d?)?)(?:\.([A-Z]{1,2}\d{2,4}))?(?::(\d{1,3}))?$")

# Conductor cross-section, e.g. 1.50 mm²   2.5 mm²
RE_XSECTION = re.compile(r"^(\d+(?:[.,]\d+)?)\s*mm\s*2?$|^(\d+(?:[.,]\d+)?)mm²$")

# Wire colour words observed in the schematics (German, as printed)
WIRE_COLOURS = {
    "sw": "schwarz / black",
    "bl": "blau / blue",
    "br": "braun / brown",
    "rt": "rot / red",
    "ws": "weiss / white",
    "gr": "grau / grey",
    "gn": "gruen / green",
    "ge": "gelb / yellow",
    "vi": "violett / violet",
    "or": "orange / orange",
    "rs": "rosa / pink",
    "tk": "tuerkis / turquoise",
    "blau": "blau / blue",
    "braun": "braun / brown",
    "schwarz": "schwarz / black",
    "rot": "rot / red",
    "grau": "grau / grey",
    "weiss": "weiss / white",
    "gelb": "gelb / yellow",
    "gruen": "gruen / green",
    "grün": "gruen / green",
    "violett": "violett / violet",
    "orange": "orange",
    "rosa": "rosa / pink",
    "tuerkis": "tuerkis / turquoise",
    "grunge": "gruen / green",
    "gnge": "gruen-gelb / green-yellow",
    "wsbr": "weiss-braun",
}

# Placeholder used by CIM-TEAM for "not fitted / option not present"
PLACEHOLDER_TOKENS = {"X", "x", ""}

# --------------------------------------------------------------------------
# Documents
# --------------------------------------------------------------------------
DOCUMENTS = [
    # (pdf filename, dockey, title-code)
    ("Cicuit Diagram +FB.pdf",            "+FB",       "R700_7759_IEC_UL_FB"),
    ("Circuit Diagram +Ax.pdf",           "+Ax",       "R700_7758_IEC_AX_8039G38I902_p"),
    ("Circuit Diagram +BA, Cx, DA.pdf",   "+BA_Cx_DA", "R700_7758_IEC_UL_BA_CX_DA_8039G38J415_p"),
    ("Circuit Diagram +EA.pdf",           "+EA",       "R700_7758_IEC_UL_EA_8039G38E915_p"),
    ("Circuit Diagram +FA.pdf",           "+FA",       "R700_7759_IEC_UL_FA"),
    ("Circuit Diagram +Jx.pdf",           "+Jx",       "R700_7758_IEC_UL_JX_039G38F308_p"),
]

DOC_TITLE_CODE = {dockey: code for (_f, dockey, code) in DOCUMENTS}

# Machine sections referenced by the Maschinenschema sheet
SECTION_NAMES = {
    "+FB": ("Lackmodul / Coating module (Modul 3)", "DE"),
    "+FA": ("Ausleger / Delivery", "DE"),
    "+EA": ("Druckwerk / Printing unit (Modul 2)", "DE"),
    "+JX": ("1. Druckmodul + Anlage / 1st printing module + feed register (Modul 1)", "DE"),
    "+Jx": ("1. Druckmodul + Anlage / 1st printing module + feed register (Modul 1)", "DE"),
    "+CX": ("Druckwerk / Printing unit", "DE"),
    "+Cx": ("Druckwerk / Printing unit", "DE"),
    "+BA": ("Druckwerk / Printing unit", "DE"),
    "+AB": ("Aggregate / Aggregats", "DE"),
    "+ZX": ("Leitstand / Central control console", "DE"),
    "+AX": ("Leitstand / Central control console", "DE"),
    "+Ax": ("Leitstand / Central control console", "DE"),
    "+DA": ("Hauptschaltschrank / Main switch cabinet", "DE"),
}

# --------------------------------------------------------------------------
# Section -> topic classification, by title-block document/section title
# --------------------------------------------------------------------------
SECTION_TOPICS = [
    ("INHALTSVERZEICHNIS", "Contents", "TOC"),
    ("ÄNDERUNGSINDEX", "Modification index", "REVISION"),
    ("ÄNDERUNGS INDEX", "Modification index", "REVISION"),
    ("MASCHINENSCHEMA", "Machine diagram", "MACHINE_LAYOUT"),
    ("ANORDNUNGSPLAN", "Disposition plan", "ARRANGEMENT"),
    ("ALLGEMEINE HINWEISE", "General indications", "LEGEND"),
    ("INDEX", "Index", "INDEX"),
    ("SPANNUNGSVERSORGUNG", "Voltage supply", "POWER_SUPPLY"),
    ("ERDUNG", "Earthing / potential compensation", "EARTHING"),
    ("FARBABSTIMMLEUCHTE", "Colour matching lamp", "LIGHTING"),
    ("BEDIENUNGSEINHEIT", "Control unit", "CONTROL_UNIT"),
    ("NEIGUNGSEINSTELLUNG", "Inclination adjustment", "OPTION"),
    ("COLORPILOT", "ColorPilot", "OPTION"),
    ("BEIPACK", "Accessories", "ACCESSORIES"),
    ("KLEMMLEISTE", "Terminal strip", "TERMINALS"),
    ("REFERENZMODUL", "Reference module", "REFERENCE_MODULE"),
]
