"""
Label grammar + title-block field rules for the manroland R700 IEC/UL
circuit diagrams (CIM-TEAM CAE export, 1351 A3 sheets).

Everything here was derived by measurement, not assumption.
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Title-block token patterns
# ---------------------------------------------------------------------------
T_DATE = re.compile(r"^(\d{1,2})\.(\d{1,2})\.(\d{2,4})$")
# document code is alphanumeric: 8039G38K159 / 039G38F308 / 8039G38I902
T_DOCCODE = re.compile(r"^(?=\S{8,14}$)(?=.*\d)(?=.*[A-Z])\d{3,5}[A-Z0-9]\d?[A-Z0-9]{2}\d{2,4}$")
T_DOCCODE_LOOSE = re.compile(r"^(?=.*\d)(?=.*[A-Z])[0-9A-Z]{8,14}$")
T_NUM = re.compile(r"^\d{1,4}$")
T_SECTION = re.compile(r"^[+\-][A-Za-z]{1,3}(?:[,_][A-Za-z]{1,3})*$")
T_MACHINE = re.compile(r"^=?R700$")
T_PAPER = re.compile(r"^DIN\s?A3$")
T_NORMROW = re.compile(r"^B2_\d{2}\s*:?$")
T_NORMODERN = re.compile(r"^(IEC|UL)\s*\([NMW]\)$")
# Sentinel for an empty title-block cell
T_EMPTY_MARK = re.compile(r"^[Xx]$")

# ---------------------------------------------------------------------------
# Circuit-area label grammar
# ---------------------------------------------------------------------------
# Cross reference to another sheet:  /13.G  (sheet 13, column G)
RE_XREF = re.compile(r"^/(\d{1,3})\.([A-H])(?::([0-9A-Za-z/]{1,6}))?$")

# Path / line number (Rennzahl): #67
RE_PATH = re.compile(r"^#(\d{1,4})$")

# Pin pair on a plug:  2/5  (pin 2 of 5)
RE_PINPAIR = re.compile(r"^(\d{1,3})/(\d{1,3})$")

# Conductor cross-section: 1.50 mm2 / 2,5 mm²
RE_XSECTION = re.compile(r"^(\d+(?:[.,]\d+)?)\s*mm\s*[2²]$")

# Potential / net designation, the leading atom of a dotted chain.
RE_NET_CORE = re.compile(
    r"^(?P<sign>[+\-])?(?P<net>"
    r"\d{1,3}\s?V"
    r"|[LMH]\d{1,3}[A-Z]?(?:[+\-](?:/\d+)?)?"
    r"|\d{1,3}[A-Z]{1,2}[+\-](?:/\d+)?"
    r"|PE|N"
    r")$"
)

# Sign-less device tag:  A497/1  X602  X001  A358/06
RE_DEV_SIGNED = re.compile(
    r"^(?P<sign>[+\-])(?P<cls>[A-Z]{1,3})(?P<num>\d{1,4})"
    r"(?:/(?P<sub>\d{1,2}))?"
    r"(?:\.(?P<loc>[A-Z]{1,3}\d{1,4}))?"
    r"(?::(?P<pin>[0-9A-Za-z]{1,6}))?$"
)
RE_DEV_BARE = re.compile(
    r"^(?P<cls>[A-Z]{1,3})(?P<num>\d{1,4})"
    r"(?:/(?P<sub>\d{1,2}))?"
    r"(?:\.(?P<loc>[A-Z]{1,3}\d{1,4}))?"
    r"(?::(?P<pin>[0-9A-Za-z]{1,6}))?$"
)

# A dotted reference chain, e.g.  24V.X1.A566:4   X26.A342:1   0V.X12.A343:1
# Segments may be alphanumeric in any arrangement: the documents really do use
# forms such as  24V.X85.1.A345:13   (numeric segment)  and
# 0V.X8.A225\1:2  (backslash sub-unit separator, occasionally doubled by the
# exporter).  Being permissive here is safe because the *head* still has to
# match RE_NET_CORE (or the leading device class) before anything is accepted.
RE_DOTTED = re.compile(
    r"^[+\-]?[0-9A-Za-z+/\\]{1,14}"
    r"(?:\.[0-9A-Za-z\\]{1,10}){1,4}"
    r"(?::[0-9A-Za-z]{1,6})?$"
)

# A trailing qualifier after a potential, e.g. "24V DC", "24V AC".
RE_NET_QUALIFIER = re.compile(r"^(?P<net>[0-9A-Za-z+/]+)\s+(?P<qual>DC|AC)$")

# A potential with a conductor index, e.g. "PE/3" (third protective-earth run).
RE_NET_INDEX = re.compile(r"^(?P<net>[A-Za-z0-9+/]+?[+\-]?)/(?P<idx>\d{1,2})$")

# Dotted reference with a *placeholder* terminal, e.g. the exporter emits
# "24V.A124:( )", "0V.A124:(+)", "24V.A124:" and "24V.X1.M.:" on schematic
# sheets where the pin is not yet assigned.  These are still real wire labels.
RE_DOTTED_PLACEHOLDER = re.compile(
    r"^(?P<head>[0-9A-Za-z+/]{1,10})"
    r"(?:\.[0-9A-Za-z\\]{0,10}){1,4}"     # a segment may itself be a bare "M."
    r"(?::|:\s*\(?\s*[+\-]?\s*\)?)?$"
)

# Space that the exporter injects after the dot inside a reference: "24V. X001:23"
RE_DOTTED_SPACE = re.compile(r"([0-9A-Za-z+\-/])\.\s+([A-Z0-9])")

# Terminal part that is a placeholder rather than a real pin.
PLACEHOLDER_TERMINALS = {"", "(", ")", "( )", "(+)", "(-)", "(+ )", "(- )",
                         "+", "-", "M", "."}

# Composite potential lists written as one label, e.g. "400V,24V" / "PE,0V".
RE_NET_LIST_SPLIT = re.compile(r"[,;]\s*")

# Word -> colour, German as printed on the sheets
WIRE_COLOURS = {
    "blau": ("BL", "blau", "blue"),
    "braun": ("BR", "braun", "brown"),
    "schwarz": ("SW", "schwarz", "black"),
    "rot": ("RT", "rot", "red"),
    "grau": ("GR", "grau", "grey"),
    "weiss": ("WS", "weiss", "white"),
    "gelb": ("GE", "gelb", "yellow"),
    "gruen": ("GN", "gruen", "green"),
    "grün": ("GN", "gruen", "green"),
    "violett": ("VI", "violett", "violet"),
    "orange": ("OR", "orange", "orange"),
    "rosa": ("RS", "rosa", "pink"),
    "tuerkis": ("TK", "tuerkis", "turquoise"),
    "gnge": ("GNG", "gruen-gelb", "green-yellow"),
    "wsbr": ("WSBR", "weiss-braun", "white-brown"),
    "brbl": ("BRBL", "braun-blau", "brown-blue"),
}

# ---------------------------------------------------------------------------
# Device order codes / part-number markers
# ---------------------------------------------------------------------------
# The drawings DO carry manroland order codes on the disposition plans, and
# occasionally beside a device on a wiring sheet.  Measured shape: 4 digits,
# a capital letter, then 5-9 further alphanumerics, e.g.
#   8037D44A002   8037B44A131   8237B447093   8098O442024   8337M518169
# They are printed at the foot of a connector block, not captioned, and there is
# no leader line binding a code to one device.  Present on only 9 of 1,351 sheets
# (20 distinct codes, 45 tokens).
# Document codes match the same shape, so they must be excluded explicitly.
RE_ORDER_CODE = re.compile(r"^\d{4}[A-Z][0-9A-Z]{5,9}$")

DOCUMENT_CODES = {"8039G38K159", "8039G38I902", "8039G38J415", "8039G38E915",
                  "8039G38K212", "039G38F308", "8039G38I415", "8039G38I411"}

# Explicit marker meaning "this connector has no orderable part number".
RE_NO_PART = re.compile(r"^Stecker_noPart[_A-Za-z0-9+]*$")

# Device-class letters as used by the CAE system (IEC 81346 / DIN 40719)
DEVICE_CLASSES = {
    "A": "Baugruppe / assembly, module, PC board",
    "B": "Umformer / transducer, sensor",
    "C": "Kapazitaet / capacitor",
    "D": "Digital / binary element",
    "E": "Sonstiges / miscellaneous, lamp",
    "F": "Schutz / protection device (fuse, circuit breaker)",
    "G": "Stromversorgung / power supply",
    "H": "Signalleuchte / indicator lamp",
    "K": "Relais / relay, contactor",
    "M": "Motor",
    "N": "Netzteil / power unit, amplifier",
    "P": "Messgeraet / measuring instrument, meter",
    "Q": "Leistungsschalter / power switching device",
    "R": "Widerstand / resistor",
    "S": "Schalter / switch",
    "T": "Transformator / transformer",
    "U": "Umrichter / frequency converter",
    "V": "Diode / semiconductor valve",
    "W": "Kabel / cable, line, bus",
    "X": "Klemme / terminal, plug connector",
    "Y": "Magnetventil / solenoid valve, actuator",
}
