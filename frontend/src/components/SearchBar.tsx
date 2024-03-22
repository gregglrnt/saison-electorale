import React from 'react';

const SearchBar = () => {
  return (
    <div className='container-search'>``
      <input type='text' className='rounded-input' placeholder='Rechercher ma commune...'/>
      <button className='search-button'>Rechercher</button>
    </div>
  );
};

export default SearchBar;