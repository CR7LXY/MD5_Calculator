import re


def is_valid_mac(mac: str) -> bool:
    """验证MAC地址格式（如00:1A:2B:3C:4D:5E）[3](@ref)"""
    pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    return re.match(pattern, mac) is not None
