package main

import (
  "fmt"
  "net/http"
)

func main() {
  fmt.Println("hello world")

  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, you've requested: %s\n", r.URL.Path)
  })

  if err := http.ListenAndServe(":8080", nil); err != nil {
    panic(err)
  }
}
