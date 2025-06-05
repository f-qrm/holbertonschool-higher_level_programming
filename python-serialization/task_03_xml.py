#!/usr/bin/env python3
"""
Module for serializing and deserializing Python dictionaries to and from
XML files.

This module provides two main functions:
- `serialize_to_xml`: converts a dictionary into XML format and writes
it to a file.
- `deserialize_from_xml`: reads an XML file and converts it back to a
dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Each key-value pair in the dictionary becomes a tag-text pair in the XML
    structure.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to write the serialized
        data to.

    Returns:
        None
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        elements = ET.SubElement(root, key)
        elements.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Reads the XML structure and converts each tag and its text content into
    key-value pairs.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: A dictionary representation of the XML content.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dict = {}
    for child in root:
        dict[child.tag] = child.text
    return dict
