def test_uname_board(target, board):
    """Test if the expected board name is correct in uname."""
    ans = target.write("uname -a")
    assert board in ans
