package main

import (
	"html/template"
	"log"
	"net/http"
	"strings"
)

var templates = template.Must(template.ParseGlob("web/templates/*"))

func main() {
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("web/static"))))
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		serveTemplate(w, r)
	})
	log.Println("Server started on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func serveTemplate(w http.ResponseWriter, r *http.Request) {
	path := r.URL.Path
	if path == "/" {
		path = "/home"
	}
	tmpl, err := templates.Clone()
	if err != nil {
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}
	_, err = tmpl.ParseFiles("web/templates" + path + ".html")
	if err != nil {
		log.Println(err)
		http.NotFound(w, r)
		return
	}

	data := map[string]interface{}{
		"Title": strings.Title(strings.Trim(path, "/")),
	}

	err = tmpl.ExecuteTemplate(w, "base.html", data)
	if err != nil {
		log.Println(err)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
	}
}
