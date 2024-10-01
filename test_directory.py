import pytest

@pytest.mark.parametrize("directory", ["testdir", "testdir000", "0_testdir_1"])
def test_dir_create_delete(target, directory):
    """Tests mkdir and rmdir by creating a directory, asserting it was
       created and then deleting and asserting it was properly removed.

       Note: regarding best practices, using two assertions in sequence is
       not recommended. If the first assertion fails, the execution is halted
       and the following tests are not executed. There are other ways of doing
       this, such as using the pytest-check plugin.
    """
    target.write(f"mkdir {directory}")
    ans = target.write("ls")
    assert directory in ans

    target.write(f"rmdir {directory}")
    ans = target.write("ls")
    assert directory not in ans
