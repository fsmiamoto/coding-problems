package main

import "testing"

func TestDecipher(t *testing.T) {
	cases := []struct {
		input string
		want  string
	}{
		{"I ENIL SIHTHSIREBBIG S", "THIS LINE IS GIBBERISH"},
		{"LEVELKAYAK", "LEVELKAYAK"},
		{"H YPPAHSYADILO", "HAPPY HOLIDAYS"},
		{"ABCDEFGHIJKLMNOPQRSTUVWXYZ", "MLKJIHGFEDCBAZYXWVUTSRQPON"},
		{"VOD OWT SNEH HCNERF EGDIRTRAP A DNA SE", "FRENCH HENS TWO DOVES AND A PARTRIDGE "},
	}

	for _, c := range cases {
		got := Decipher(c.input)

		if got != c.want {
			t.Errorf("Expected %q but got %q for %q", c.want, got, c.input)
		}
	}
}

func TestReverseString(t *testing.T) {
	cases := []struct {
		input string
		want  string
	}{
		{"abcdef", "fedcba"},
		{"ana", "ana"},
		{"laringe", "egniral"},
	}

	for _, c := range cases {
		got := ReverseString(c.input)

		if got != c.want {
			t.Errorf("Expected %q but got %q for %q", c.want, got, c.input)
		}
	}
}

func TestSplitByHalf(t *testing.T) {
	cases := []struct {
		input string
		want  [2]string
	}{
		{"abcdef", [2]string{"abc", "def"}},
		{"golang", [2]string{"gol", "ang"}},
		{"the end", [2]string{"the", " end"}},
	}

	for _, c := range cases {
		got := SplitByHalf(c.input)

		if got != c.want {
			t.Errorf("Expected %q but got %q for %q", c.want, got, c.input)
		}
	}
}
