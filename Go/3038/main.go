package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	s, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		panic(err)
	}

	msg := string(s)

	r := strings.NewReplacer(
		"@", "a",
		"&", "e",
		"!", "i",
		"*", "o",
		"#", "u",
	)

	fmt.Print(r.Replace(msg))
}
