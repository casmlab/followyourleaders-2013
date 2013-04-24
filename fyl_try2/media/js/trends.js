$(function () {
        $('#trends-canvas').highcharts({
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Tweet Trends'
            },
            subtitle: {
                text: 'trends about '+trendValue
            },
            xAxis: {
                categories: tweetData[0],
                title: {
                    text: 'Members of Congress'
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Number of Tweets',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                }
            },
            tooltip: {
                valueSuffix: ' '
            },
            plotOptions: {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -100,
                y: 100,
                floating: true,
                borderWidth: 1,
                backgroundColor: '#FFFFFF',
                shadow: true
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'tweets about "'+trendValue+'" ',
                color: '#FF7E33',
                data: tweetData[1]
            }]
        });
    });