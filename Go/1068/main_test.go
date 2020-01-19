package main

import "testing"

func TestCheckParenthesis(t *testing.T) {
	cases := []struct {
		input   string
		want bool
	}{
		{"a+(b*c)-2-a", true},
		{"(a+b*(2-c)-2+a)*2", true},
		{"(a*b-(2+c)", false},
		{"2*(3-a))", false},
		{")3+b*(2-c)(", false},
	}

	for _, c := range cases {
		got := CheckParenthesis(c.input)

		if got != c.want {
			t.Errorf("Got %v but expected %v for %q", got,c.want,c.input)
		}
	}

}
