package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/deta/deta-go/deta"
	"github.com/deta/deta-go/service/base"
	"github.com/deta/deta-go/service/drive"
	"github.com/labstack/echo/v4"
)

var d, _ = deta.New()

func main() {
	e := echo.New()

	e.GET("/", func(ctx echo.Context) error {
		return ctx.String(http.StatusOK, "Hello, World!")
	})

	e.GET("/users", func(ctx echo.Context) error {
		db, err := base.New(d, "users")
		if err != nil {
			return ctx.String(http.StatusInternalServerError, "Internal Server Error")
		}
		var users []map[string]interface{}
		_, err = db.Fetch(&base.FetchInput{Dest: &users})
		if err != nil {
			fmt.Fprintf(os.Stderr, "error: %v\n", err)
			return ctx.String(http.StatusInternalServerError, "Internal Server Error")
		}
		return ctx.JSON(http.StatusOK, users)
	})

	e.GET("/avatars/:id", func(ctx echo.Context) error {
		id := ctx.Param("id")
		drive, _ := drive.New(d, "avatars")
		r, err := drive.Get(fmt.Sprintf("%s.png", id))
		if err != nil {
			fmt.Fprintf(os.Stderr, "error: %v\n", err)
			return ctx.String(http.StatusInternalServerError, "Internal Server Error")
		}
		defer r.Close()
		return ctx.Stream(http.StatusOK, "image/png", r)
	})
	
	fmt.Println("Server running at: http://localhost:8080")
	log.Fatal(e.Start(":8080"))
}
