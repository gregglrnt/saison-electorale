import './App.css'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Filler, Legend, plugins } from 'chart.js'
import { Line } from 'react-chartjs-2'
import { da, faker } from '@faker-js/faker'
import TopBar from './components/TopBar'
import SearchBar from './components/SearchBar'
import MapChart from './components/FranceMap'
import DiscreteSlider from './components/DiscreteSlider.js'
import './graph-script.js'
import React from 'react'
/*ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Filler,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top' as const,
    },
    title: {
      display: true,
      text: 'Nombre de votants en fonction des régions',
    },
  },
};

const regions = ['Ile-de-France', 'Bretagne', 'Normandie', 'Nouvelle-Aquitaine', 'Occitanie'];

export const data = {
  regions,
  datasets: [
    {
      fill: true,
      label: 'Map test',
      data: regions.map(() => faker.datatype.number({ min: 0, max: 1000})),
      borderColor: 'rgb(53, 162, 235)',
      backgroundColor: 'rgba(53, 162, 235, 0.5)',
    },
  ],
}; */

const App = () => {
  return (
    <div className="app">
        <TopBar />
        <SearchBar />
        <MapChart />
        <DiscreteSlider />
    </div>
  )
}

export default App