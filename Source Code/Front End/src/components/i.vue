<template>
  <body>
    <div id="main">

      <h1>TNL Stock Predictor</h1>
      <img src="@/assets/1.png" alt="generic stock graph" id="pic">
      <br>

      <div id="company">
        <p>Select a company:</p>
        <select v-model="selected">
          <option v-for="company in companys" v-bind:key="company.text" v-bind:value="company.value">
            {{ company.text }}
          </option>
        </select>
        <br><br>
        <div class="mt-3">Company: <strong>{{ selected }}</strong></div>
      </div>

      <div id="day">
        <p>Select how many days (up to 7):</p>
        <select v-model="selected1">
          <option v-for="day in days" v-bind:key="day.text" v-bind:value="day.value">
            {{ day.text }}
          </option>
        </select>
        <br><br>
        <div class="mt-2">Day(s): <strong>{{ selected1 }}</strong></div>
      </div>

      <br>
      <div>
        <button v-on:click="getPrediction(selected, selected1)" class="btn">Submit</button>
        <p>Price: {{ price }}</p>
        <p>Sentiment: {{ sentiment }}</p>
        <p v-html="tweet">Tweet: {{ tweet }}</p>
        <!-- <p>Graph: {{ merged }}</p> -->
        <GChart type="ScatterChart" :data="merged" :options="chartOptions" :resizeDebounce="500"/>
        <!-- <p>Xs: {{ xs }}</p> -->
        <!-- <p>Ys: {{ ys }}</p> -->
      </div>

    </div>
  </body>
</template>

<style>
  body {
    font-family: Garamond;
    font-size: 20px;
  }
  #sel {
    font-size: 24px;
  }
  #pic {
    width: 25%
  }
  h1 {
    font-size: 50px;
  }
  button {
    height: 40px;
    width: 140px;
    font-size: 20px;
  }
</style>

<script>
import axios from 'axios'
import { GChart } from 'vue-google-charts'
export default {
  name: 'i',
  components: {
    GChart
  },
  data () {
    return {
      selected: null,
      selected1: null,
      price: null,
      sentiment: null,
      tweet: null,
      xs: null,
      ys: null,
      merged: null,
      companys: [
        { value: null, text: 'Please select an option' },
        { value: 'AAPL', text: 'Apple' },
        { value: 'MSFT', text: 'Microsoft' },
        { value: 'GOOG', text: 'Google' },
        { value: 'FB', text: 'Facebook' },
        { value: 'COF', text: 'Capital One' },
        { value: 'ATVI', text: 'Activision' }
      ],
      days: [
        { value: null, text: 'Please select a day' },
        { value: 1, text: '1' },
        { value: 2, text: '2' },
        { value: 3, text: '3' },
        { value: 4, text: '4' },
        { value: 5, text: '5' },
        { value: 6, text: '6' },
        { value: 7, text: '7' }
      ],
      chartData: [
        ['Year', 'Sales'],
        [ '2014', 1000 ],
        [ '2015', 1170 ],
        [ '2016', 660 ],
        [ '2017', 1030 ]
      ],
      chartOptions: {
        chart: {
          title: 'Company Stock'
        }
      }
    }
  },
  methods: {
    leadingZero (n) {
      return n < 10 ? '0' + n : n
    },
    getPrediction (stock, inc) {
      var datetime = new Date()
      var month = datetime.getMonth()
      var day = datetime.getDate()
      month = month + 1
      month = month < 10 ? '0' + month : month
      day = day + inc
      day = day < 10 ? '0' + day : day
      var dateForm = datetime.getFullYear() + '-' + month + '-' + day
      const path = 'http://localhost:5000/predict/' + stock + '/' + dateForm
      axios.get(path)
        .then(response => {
          this.price = response.data.price
          this.sentiment = response.data.sentiment
          this.tweet = response.data.tweet
          this.xs = response.data.xs
          this.ys = response.data.ys
          this.merged = response.data.merged
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
