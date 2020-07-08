package main

import "fmt"

func main() {
	var valores [4]int

	for i := range valores {
		fmt.Scanf("%d", &valores[i])
	}

	respostas := make(chan bool)

	go func() {
		respostas <- formaTriangulo(valores[0], valores[1], valores[2])
	}()
	go func() {
		respostas <- formaTriangulo(valores[0], valores[1], valores[3])
	}()
	go func() {
		respostas <- formaTriangulo(valores[0], valores[3], valores[2])
	}()
	go func() {
		respostas <- formaTriangulo(valores[3], valores[1], valores[2])
	}()

	for i := 0; i < 4; i++ {
		r := <-respostas
		if r {
			fmt.Println("S")
			return
		}
	}
	fmt.Println("N")
}

func formaTriangulo(a, b, c int) bool {
	return abs(b-c) < a && a < b+c &&
		abs(a-c) < b && b < a+c &&
		abs(a-b) < c && c < a+b
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
