from ragger import ApplicationError

ERRORS = (
    ApplicationError(0x6985, 'SW_DENY'),
    ApplicationError(0x6A86, 'SW_WRONG_P1P2'),
    ApplicationError(0x6A87, 'SW_WRONG_DATA_LENGTH'),
    ApplicationError(0x6D00, 'SW_INS_NOT_SUPPORTED'),
    ApplicationError(0x6E00, 'SW_CLA_NOT_SUPPORTED'),
    ApplicationError(0xB000, 'SW_WRONG_RESPONSE_LENGTH'),
    ApplicationError(0xB001, 'SW_DISPLAY_BIP32_PATH_FAIL'),
    ApplicationError(0xB002, 'SW_DISPLAY_ADDRESS_FAIL'),
    ApplicationError(0xB003, 'SW_DISPLAY_AMOUNT_FAIL'),
    ApplicationError(0xB004, 'SW_WRONG_TX_LENGTH'),
    ApplicationError(0xB005, 'SW_TX_PARSING_FAIL'),
    ApplicationError(0xB006, 'SW_TX_HASH_FAIL'),
    ApplicationError(0xB007, 'SW_BAD_STATE'),
    ApplicationError(0xB008, 'SW_SIGNATURE_FAIL')
)
