from idioms.paths import word_count_by_file, write_notes


def test_writes_and_reads_files_in_a_temporary_folder(tmp_path):
    # tmp_path is a pytest fixture: a fresh, empty pathlib.Path for each test.
    folder = tmp_path / "notes"
    written = write_notes(folder, {"monday": "tea and toast", "tuesday": "code"})

    assert [p.name for p in written] == ["monday.txt", "tuesday.txt"]
    assert all(p.suffix == ".txt" and p.parent == folder for p in written)
    assert word_count_by_file(folder) == {"monday": 3, "tuesday": 1}
