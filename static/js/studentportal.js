document.addEventListener('DOMContentLoaded', function () {
    const studentLevel = parseInt(document.getElementById('chartContainer').dataset.level);
    const courseDuration = parseInt(document.getElementById('chartContainer').dataset.duration);
  
    let levelSteps = [];
    let levelLabels = [];
  
    for (let i = 1; i <= courseDuration; i++) {
      const level = i * 100;
      levelSteps.push(level);
      levelLabels.push(i === courseDuration ? "Graduation" : `${level} Level`);
    }
  
    // Nicer color palette: one color per level
    const distinctColors = [
      "#4e79a7",  // 100L
      "#59a14f",  // 200L
      "#f28e2b",  // 300L
      "#e15759",  // 400L
      "#b07aa1",  // 500L (optional)
      "#76b7b2"   // Graduation
    ].slice(0, levelSteps.length);  // match duration
  
    const options = {
      chart: {
        type: 'bar',
        height: 320,
        toolbar: { show: false },
        events: {
          mounted: function (chartContext, config) {
            const legendLabels = document.querySelectorAll('.apexcharts-legend-text');
            legendLabels.forEach((label, index) => {
              label.style.color = distinctColors[index];
              label.style.fontWeight = 'bold';
            });
          }
        }
      },
      plotOptions: {
        bar: {
          horizontal: true,
          borderRadius: 6,
          barHeight: '60%',
          distributed: true
        }
      },
      colors: distinctColors,
      dataLabels: {
        enabled: true,
        style: {
          colors: ['#000']
        }
      },
      series: [{
        data: levelSteps
      }],
      xaxis: {
        categories: levelLabels,
        labels: { show: false }
      },
      yaxis: {
        categories: levelLabels,
        labels: {
          style: {
            colors: distinctColors,
            fontSize: '14px'
          }
        }
      },
      legend: {
        show: true,
        position: 'bottom'
      },
      title: {
        text: 'Academic Progression',
        align: 'center',
        style: {
          fontSize: '16px',
          color: '#76b7b2'
        }
      }
    };
  
    new ApexCharts(document.querySelector("#progressRoadmapChart"), options).render();
  });
  