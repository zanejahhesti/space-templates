package main

import (
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", root)  // Register the root handler
	log.Println("Running at: http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))  // Start the server
}

func root(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("Hello World!"))
	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
	}
	
}
