

//   KPI Chart
function renderRadialKPIChart(id, color = '#1abc9c') {
    const el = document.getElementById(id);
    if (!el) return;
  
    const value = parseInt(el.dataset.value || 0);
    const label = el.dataset.label || "Total";
  
    const options = {
      chart: {
        type: 'radialBar',
        height: 100,
        offsetY: -20
      },
      series: [100],  // Always full circle
      labels: [label],
      plotOptions: {
        radialBar: {
          hollow: {
            size: '40%',
            background: 'transparent',
          },
          track: {
            background: '#f0f0f0',
            strokeWidth: '100%'
          },
          dataLabels: {
            name: {
              offsetY: 50,
              fontSize: '18px',
              color: '#111',
            },
            value: {
              offsetY: -10,
              fontSize: '30px',
              fontWeight: 700,
              color: '#111',
              formatter: () => value.toLocaleString()
            }
          }
        }
      },
      colors: [color],
      stroke: {
        lineCap: 'round'
      }
    };
  
    new ApexCharts(el, options).render();
  }
renderRadialKPIChart("academicStaffKPI", "#3498db");       // Blue
renderRadialKPIChart("nonAcademicStaffKPI", "#e67e22");    // Orange
renderRadialKPIChart("totalStudentsKPI", "#2ecc71");       // Green





document.addEventListener("DOMContentLoaded", function () {
    // === GENDER DONUT CHART ===
    const genderEl = document.getElementById("genderPieChart");
    if (genderEl) {
      const male = parseInt(genderEl.dataset.male || 0);
      const female = parseInt(genderEl.dataset.female || 0);
  
      const genderOptions = {
        chart: { type: 'donut', height: 350 },
        series: [male, female],
        labels: ['Male', 'Female'],
        colors: ['#2ecc71', '#e67e22'],
        legend: { position: 'bottom',
            labels: {
                colors: ['#e67e22', '#2ecc71'], 
                useSeriesColors: false,
              },
         },
        
        title: {
          text: 'Students by Gender',
          align: 'center',

          style: {
            fontSize: '16px',
            fontWeight: 'bold',
            color: 'white',

          }
        }
      };
  
      new ApexCharts(genderEl, genderOptions).render();
    }
  
    // === DEPARTMENT BAR CHART ===
    const deptEl = document.getElementById("departmentBarChart");
    if (deptEl) {
      const rawLabels = deptEl.dataset.labels || "";
      const rawValues = deptEl.dataset.values || "";
  
      // Split CSV strings from Django
      const labels = rawLabels.split(",").map(label => label.trim());
      const values = rawValues.split(",").map(val => parseInt(val));
  
      const deptOptions = {
        chart: { 
            type: 'bar', height: 350,
            toolbar: {
                show: false  // 👈 Hides the download/export toolbar
              } 
        },
        series: [{
          name: 'Students',
          data: values
        }],
        xaxis: {
          categories: labels,
          labels: {
            rotate: -45,
            style: {
              fontSize: '12px',
              colors: '#ffffff'

            }
          }
        },
        colors: ['#3498db'],
        title: {
          text: 'Students by Department',
          align: 'center',
          style: {
            fontSize: '16px',
            fontWeight: 'bold',
            color: 'white'

          }
        }
      };
  
      new ApexCharts(deptEl, deptOptions).render();
    }
  });
  
