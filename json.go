package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

type Miner struct {
	Worker           string
	Time             int
	LastSeen         int
	ReportedHashRate int
}

type MinerSlice struct {
	Data []Miner
}

//only declaration but not assignment is allowed outside function body
var base_api string
var pool_stat string
var miner_stat string

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {

	base_api = "https://api.ethermine.org"
	pool_stat = "/poolStats"
	miner_stat = "/miner/0x3DFDedeBD8c6BF9F31844161962762c700D97cb4/workers"

	url := base_api + miner_stat

	resp, err := http.Get(url)
	checkErr(err)

	//using ioutil to read bytes
	fmt.Printf("Retrieving data from url: %v\n", url)
	bytes, err1 := ioutil.ReadAll(resp.Body)

	checkErr(err1)
	defer resp.Body.Close()

	//converting bytes into string text
	//text := string(bytes)
	//fmt.Println(text)

	//functions to bu used to pack and unpack json to interface
	//func Unmarshal(data []byte, v interface{}) error //parse json data
	//func Marshal(v interface{}) ([]byte, error) //produce json data

	var s MinerSlice
	err2 := json.Unmarshal(bytes, &s)
	checkErr(err2)

	//fmt.Println(s)

	for k := range s.Data {
		fmt.Printf("Machine name is: %v Speed is %v Mh/s\n", s.Data[k].Worker, s.Data[k].ReportedHashRate/1000000)
	}

}
