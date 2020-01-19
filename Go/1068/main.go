package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main(){
	r := bufio.NewReader(os.Stdin)

	for {
		line, err := r.ReadString('\n')
		if err != nil {
			break
		}

		input := strings.TrimRight(line,"\n")

		if !CheckParenthesis(input) {
			fmt.Println("incorrect")
			continue
		}

		fmt.Println("correct")
	}
}

func CheckParenthesis(s string) (correct bool){
	stack := NewStack()

	for _, r := range s {
		switch r {
		case '(':
			stack.Push(r)
		case ')':
			if stack.Top() != '(' {
				return false
			}
			stack.Pop()
		default:
			continue
		}
	}

	if stack.Size() != 0 {
		return false
	}

	return true
}

type Stack []rune

func NewStack() *Stack {
	return &Stack{}
}

func (s *Stack) Push(r rune) {
	*s = append(Stack{r}, *s...)
}

func (s *Stack) Pop() rune {
	pop := (*s)[0]
	*s = (*s)[1:]
	return pop
}

func (s *Stack) Size() int {
	return len(*s)
}

func (s *Stack) Top() rune {
	if len(*s) == 0 {
		return 0
	}

	return (*s)[0]
}
