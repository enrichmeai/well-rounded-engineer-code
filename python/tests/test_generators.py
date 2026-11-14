from idioms.generators import fibonacci, first, flatten, non_blank_lines


def test_an_endless_generator_is_fine_if_you_only_take_some():
    assert first(10, fibonacci()) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_yield_from_flattens_nested_lists():
    assert list(flatten([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]


def test_generators_are_lazy():
    seen = []

    def noisy():
        for n in range(3):
            seen.append(n)
            yield n

    gen = noisy()
    assert seen == []  # nothing has run yet
    next(gen)
    assert seen == [0]


def test_generator_expression_skips_blank_lines():
    assert list(non_blank_lines(["a\n", "   \n", " b "])) == ["a", "b"]
