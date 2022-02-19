package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	r := bufio.NewReader(os.Stdin)
	for i := 0; i < n; i++ {
		line, _ := r.ReadString('\n')
		msg := strings.TrimRight(line, "\n")
		fmt.Println(Decipher(msg))
	}

}

func Decipher(s string) string {
	halves := SplitByHalf(s)

	var builder strings.Builder
	for _, h := range halves {
		builder.WriteString(ReverseString(h))
	}
	return builder.String()
}

func ReverseString(s string) string {
	var builder strings.Builder

	for i := len(s) - 1; i >= 0; i-- {
		builder.WriteByte(s[i])
	}

	return builder.String()
}

func SplitByHalf(s string) [2]string {
	var firstHalf, secondHalf strings.Builder

	half := len(s) / 2

	for i := 0; i < half; i++ {
		firstHalf.WriteByte(s[i])
	}

	for i := half; i < len(s); i++ {
		secondHalf.WriteByte(s[i])
	}

	return [2]string{firstHalf.String(), secondHalf.String()}
}
