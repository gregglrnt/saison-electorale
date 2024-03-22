import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';

function valuetext(value: number) {
    return `${value}°C`;
  }
  
const DiscreteSlider = () => {

    const marks = [
        { value: 2012, label: 'Présidentielle 2012' },
        { value: 2017, label: 'Présidentielle 2017' },
        { value: 2022, label: 'Présidentielle 2022' }
    ]
    return (
      <Box sx={{ width: 300 }}>
        <Slider
          aria-label="Météo"
          defaultValue={0}
          getAriaValueText={valuetext}
          valueLabelDisplay="auto"
          shiftStep={5}
          step={5}
          marks={marks}
          min={2012}
          max={2022}
          sx={{
            '& .MuiSlider-markLabel': {
                textAlign: 'center'
              }
          }}
        />
      </Box>
    );
}

export default DiscreteSlider