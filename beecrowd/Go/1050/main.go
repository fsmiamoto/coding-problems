package main

import "fmt"

var ddds = map[string]string{
	"61": "Brasilia",
	"71": "Salvador",
	"11": "Sao Paulo",
	"21": "Rio de Janeiro",
	"32": "Juiz de Fora",
	"19": "Campinas",
	"27": "Vitoria",
	"31": "Belo Horizonte",
}

func main() {
	var input string
	fmt.Scanf("%s", &input)

	d, ok := ddds[input]
	if !ok {
		fmt.Println("DDD nao cadastrado")
		return
	}

	fmt.Println(d)
}
