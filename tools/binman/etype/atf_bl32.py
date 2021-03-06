# SPDX-License-Identifier: GPL-2.0+
# Copyright (C) 2022 Texas Instruments Incorporated - https://www.ti.com/
#
# Entry-type module for OP-TEE Trusted OS firmware blob
#

from binman.etype.blob_named_by_arg import Entry_blob_named_by_arg

class Entry_atf_bl32(Entry_blob_named_by_arg):
    """Entry containing an OP-TEE Trusted OS (TEE) BL32 blob

    Properties / Entry arguments:
        - atf-bl32-path: Filename of file to read into entry. This is typically
            called bl32.bin or bl32.elf

    This entry holds the run-time firmware, typically started by U-Boot SPL.
    See the U-Boot README for your architecture or board for how to use it. See
    https://github.com/OP-TEE/optee_os for more information about OP-TEE.
    """
    def __init__(self, section, etype, node):
        super().__init__(section, etype, node, 'atf-bl32')
        self.external = True
