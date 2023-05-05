def write_to_log(warning_text, info_text, debug_text):
    import logging
    logging.warning(warning_text)
    logging.info(info_text)
    logging.debug(debug_text)
