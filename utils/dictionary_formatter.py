def dictionary_formatter(input_dictionary: dict[str, str], separator: str = "\t", header: bool = True) -> str:
    if not input_dictionary:
        return "No currencies available."
    lines = []
    if header:
        lines.append(f"Code{separator}Currency")
    for code, currency in sorted(input_dictionary.items()):
        lines.append(f"{currency}{separator}{code}")
    return "\n".join(lines)