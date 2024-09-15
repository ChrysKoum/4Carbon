import 'jsvectormap/dist/css/jsvectormap.css';
import '../js/us-aea-en';
import greeceMap from '../images/greece_map.png';


const MapOne = () => {

  return (
    <div className="col-span-12 rounded-sm border border-stroke bg-white py-6 px-7.5 shadow-default dark:border-strokedark dark:bg-boxdark xl:col-span-7">
      <h4 className="mb-2 text-xl font-semibold text-black dark:text-white">
        Region labels
      </h4>
      <div id="mapOne" className="mapOne map-btn h-100">
      <img src={greeceMap} alt="greece heat map" />
      </div>
    </div>
  );
};

export default MapOne;
