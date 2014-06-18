"""Module for inspecting PCI device info"""

from hwinfo.util import CommandParser

class ParserException(Exception):
    pass

class LspciVVParser(CommandParser):
    """Parser object for the output of lspci -vv"""

    ITEM_REGEXS = [
        r'(?P<pci_device_bus_id>([0-9][0-9]:[0-9][0-9]\.[0-9]))\ (?P<pci_device_type>[\w\ ]*):\ (?P<pci_device_string>(.*))\n',
        r'Product\ Name:\ (?P<pci_device_vpd_product_name>(.)*)\n',
        r'Subsystem:\ (?P<pci_device_sub_string>(.)*)\n',
    ]

    ITEM_SEPERATOR = r'^\n'

    MUST_HAVE_FIELDS = [
        'pci_device_bus_id',
        'pci_device_type',
        'pci_device_string',
    ]