<template>
  <div>

    <!--&lt;!&ndash;Stats cards&ndash;&gt;
    <div class="row">
      <div class="col-md-6 col-xl-3" v-for="stats in statsCards" :key="stats.title">
        <stats-card>
          <div class="icon-big text-center" :class="`icon-${stats.type}`" slot="header">
            <i :class="stats.icon"></i>
          </div>
          <div class="numbers" slot="content">
            <p>{{stats.title}}</p>
            {{stats.value}}
          </div>
          <div class="stats" slot="footer">
            <i :class="stats.footerIcon"></i> {{stats.footerText}}
          </div>
        </stats-card>
      </div>
    </div>-->

    <!--Charts-->
    <div class="row">

      <div class="col-12">
        <chart-card title="10s BTC 成交累计量"
                    sub-title=""
                    :chart-data="orderChart.data"
                    :chart-options="orderChart.options">
          <span slot="footer">
            <i class="ti-reload"></i> Updated 10 seconds ago
          </span>
        </chart-card>
      </div>

      <!--<div class="col-md-6 col-12">
        <chart-card title="Email Statistics"
                    sub-title="Last campaign performance"
                    :chart-data="preferencesChart.data"
                    chart-type="Pie">
          <span slot="footer">
            <i class="ti-timer"></i> Campaign set 2 days ago</span>
          <div slot="legend">
            <i class="fa fa-circle text-info"></i> Open
            <i class="fa fa-circle text-danger"></i> Bounce
            <i class="fa fa-circle text-warning"></i> Unsubscribe
          </div>
        </chart-card>
      </div>

      <div class="col-md-6 col-12">
        <chart-card title="2015 Sales"
                    sub-title="All products including Taxes"
                    :chart-data="activityChart.data"
                    :chart-options="activityChart.options">
          <span slot="footer">
            <i class="ti-check"></i> Data information certified
          </span>
          <div slot="legend">
            <i class="fa fa-circle text-info"></i> Tesla Model S
            <i class="fa fa-circle text-warning"></i> BMW 5 Series
          </div>
        </chart-card>
      </div>-->

    </div>

  </div>
</template>
<script>
import { StatsCard, ChartCard } from "@/components/index";
import Chartist from 'chartist';
import $ from 'jquery';
import _ from 'lodash';

export default {
  components: {
    //StatsCard,
    ChartCard
  },
  /**
   * Chart data used to render stats, charts. Should be replaced with server data
   */
  data() {

    return {
      apiData: [],
      orderChart: {
        data: {
          labels: [],
          series: []
        },
        options: {
          low: 0,
          high: 60,
          showArea: true,
          height: "245px",
          axisX: {
            showGrid: false
          },
          lineSmooth: Chartist.Interpolation.simple({
            divisor: 3
          }),
          showLine: true,
          showPoint: true
        }
      }
    };
  },

  mounted(){
    let self = this;
    self.getApiData();
    setInterval(function () {
      self.getApiData();
      self.saveApiData();
    }, 10000)
  },
  methods: {

    //冒泡排序
    bubbleSort: function(array) {
      let low = 0;
      let high = array.length - 1;
      while (low < high) {
        for (let j = low; j < high; j++) {
          if (array[j] > array[j + 1]) {
            const temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
          }
        }
        --high;
      }
      return array;
    },

    //十秒调用接口保存一次数据
    saveApiData: function(){
      let _this = this;
      $.ajax({
        url: 'http://127.0.0.1:5000/api/addCharts',
        type: 'POST',
        data: {chartsData: JSON.stringify(_this.apiData)},
        dataType: 'JSON',
        success: function(res){
          if(res.code==0){
            console.log('保存数据成功');
          }
        },
        fail: function(res){

        }
      });
    },

    getApiData: function(){
      let _this= this;
      $.ajax({
        url: 'http://127.0.0.1:5000/api/charts',
        type: 'GET',
        success: function (res) {
          let data = res.data;
          _this.apiData = res.data;
          let volume_json = {};
          let total_vol = 0.0;
          for(let i in data){
            let item = data[i];
            let volume = item[1];
            let d_time = item[2];

            let sub_time = d_time.split("T")[1].split(".")[0];
            total_vol += _.floor(volume, 8);
            volume_json[sub_time] = total_vol;
          }
          let labels = _.keys(volume_json).sort();
          let vol_series = _this.bubbleSort(_.values(volume_json));
          _this.orderChart.data.labels = labels;
          _this.orderChart.data.series = [vol_series];
        }
      });
    }
  }
};
</script>
<style>
</style>
