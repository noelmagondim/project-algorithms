from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message_1 = "AABBCC"
    saida_1 = "BAA_CCB"
    key_1 = 3

    message_2 = "ABBCCA"
    saida_2 = "AC_CBBA"
    key_2 = 4

    message_3 = "AABBCC"
    saida_3 = "CCBBAA"
    key_3 = -1

    assert encrypt_message(message_1, key_1) == saida_1
    assert encrypt_message(message_2, key_2) == saida_2
    assert encrypt_message(message_3, key_3) == saida_3

    with pytest.raises(Exception):
        encrypt_message(message_3, "4")

    with pytest.raises(Exception):
        encrypt_message(["AA", "BB"], 4)
