import { useState } from 'react';
import BrandOne from '../images/brand/brand-01.svg';
import BrandThree from '../images/brand/brand-03.svg';
import BrandFour from '../images/brand/brand-04.svg';
import BrandFive from '../images/brand/brand-05.svg';

const TableOne = () => {
  const [hoveredFee, setHoveredFee] = useState<number | null>(null);

  // Function to calculate 5% of a number
  const calculateFivePercent = (amount: number) => (amount * 0.05).toFixed(2);

  // Fees data
  const fees = [
    { company: 'Royal Caribbean', visitors: 7600, totalFee: 205200, personFee: 27, time: '09:00-12:00', carbonFootprint: '4.8%' },
    { company: 'MSC Cruises', visitors: 6762, totalFee: 209622, personFee: 31, time: '13:00-15:00', carbonFootprint: '4.5%' },
    { company: 'Carnival Cruise', visitors: 6631, totalFee: 225454, personFee: 34, time: '16:00-19:00', carbonFootprint: '4.1%' }
  ];

  return (
    <div className="rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1">
      <h4 className="mb-6 text-xl font-semibold text-black dark:text-white">
        Companies - 15/09/2024
      </h4>

      <div className="flex flex-col">
        <div className="grid grid-cols-2 rounded-sm bg-gray-2 dark:bg-meta-4 sm:grid-cols-6">
          <div className="p-2.5 xl:p-5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">Name</h5>
          </div>
          <div className="p-2.5 text-center xl:p-5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">Visitors</h5>
          </div>
          <div className="hidden p-2.5 text-center sm:block xl:p-5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">Total Fee</h5>
          </div>
          <div className="hidden p-2.5 text-center sm:block xl:p-5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">Person Fee</h5>
          </div>
          <div className="hidden p-2.5 text-center sm:block xl:p-5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">Time</h5>
          </div>
          <div className="hidden p-2.5 text-center sm:block xl:p-5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">Carbon Footprint</h5>
          </div>
        </div>

        {fees.map((fee, index) => (
          <div
            key={index}
            className="grid grid-cols-2 border-b border-stroke dark:border-strokedark sm:grid-cols-6"
            onMouseEnter={() => setHoveredFee(fee.totalFee)}
            onMouseLeave={() => setHoveredFee(null)}
          >
            <div className="flex items-center gap-3 p-2.5 xl:p-5">
              <div className="flex-shrink-0">
                <img src={index === 0 ? BrandOne : index === 1 ? BrandFive : index === 2 ? BrandFour : BrandThree} alt="Brand" />
              </div>
              <p className="hidden text-black dark:text-white sm:block">{fee.company}</p>
            </div>

            <div className="flex items-center justify-center p-2.5 xl:p-5">
              <p className="text-black dark:text-white">{fee.visitors}</p>
            </div>

            <div className="relative hidden items-center justify-center p-2.5 sm:flex xl:p-5">
              <p className="text-meta-3">€{fee.totalFee.toLocaleString()}</p>
              {hoveredFee === fee.totalFee && (
                <div className="absolute top-full mt-2 rounded bg-black text-white p-2 text-xs">
                  5% of Total Fee: €{calculateFivePercent(fee.totalFee)}
                </div>
              )}
            </div>

            <div className="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
              <p className="text-black dark:text-white">{fee.personFee}</p>
            </div>

            <div className="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
              <p className="text-black dark:text-white">{fee.time}</p>
            </div>

            <div className="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
              <p className="text-meta-5">{fee.carbonFootprint}</p>
            </div>
          </div>
        ))}
        <div className="grid grid-cols-2 border-b border-stroke dark:border-strokedark sm:grid-cols-6 opacity-50">
    
      <div className="flex items-center gap-3 p-2.5 xl:p-5">
        <div className="flex-shrink-0">
          <img src={BrandThree} alt="Brand" />
        </div>
        <p className="hidden text-black dark:text-white sm:block">Blue Star Ferries</p>
      </div>
    
      <div className="flex items-center justify-center p-2.5 xl:p-5">
        <p className="text-black dark:text-white">2,400</p>
      </div>
    
      <div className="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
        <p className="text-meta-3">€60,000</p>
      </div>
    
      <div className="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
        <p className="text-black dark:text-white">25</p>
      </div>
    
      <div className="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
        <p className="text-black dark:text-white">16:00-19:00</p>
      </div>
    
      <div className="hidden items-center justify-center p-2.5 sm:flex xl:p-5">
        <p className="text-meta-5">2.3%</p>
      </div>
    
    </div>
      </div>
    </div>
  );
};

export default TableOne;
