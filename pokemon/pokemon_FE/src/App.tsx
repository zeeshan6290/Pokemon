import React, {useEffect, useState} from 'react';
import { getData } from './Service';
import DataTable, { TableColumn } from 'react-data-table-component';

import './App.css';

interface DataRow {
  id: number,
  name: string,
  base_experience: number;
  height: string;
  weight: number;
  image_url: string;
}

const columns: TableColumn<DataRow>[] = [
  {
      name: 'ID',
      selector: row => row.id,
  },
  {
    name: 'Name',
    selector: row => row.name,
  },
  {
    name: 'Base Experience',
    selector: row => row.base_experience,
  },
  {
    name: 'Height',
    selector: row => row.height,
  },
  {
    name: 'Weight',
    selector: row => row.weight,
  },
  {
      name: 'Image',
      cell: (row: { image_url: string | undefined; name: string | undefined; }) => <img src={row.image_url} width={50} alt={row.name}></img>,
      selector: (row: { image_url: any; }) => row.image_url,
      width: '100px'
  },
];
function App() {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);
  const [totalRows, setTotalRows] = useState(0);
  const [perPage, setPerPage] = useState(10);
  const [filterBy, setFilterBy] = useState('');
  const [filterValue, setFilterValue] = useState('');
  const [search, setSearch] = useState('');
  const [currentSelectValue, setCurrentSelectValue] = useState('All');


  useEffect(() => {
    fetchData(1);
  }, [perPage])

  const filterData = () => {
   fetchData(1);
  }
  const fetchData = async (page: number) => {
    try {
    const response = await getData(page, perPage, search, filterBy, filterValue);
      setIsLoaded(true);
      setItems(response.data);
      setTotalRows(response.total);
    } catch(error) {
        setIsLoaded(true);
    }
  }

  const handlePageChange = (page: any) => {
    fetchData(page);
  }

  const handlePerRowsChange = async (newPerPage: React.SetStateAction<number>, page: any) => {
    setPerPage(newPerPage);
  }

  if (!isLoaded) {
    return <div>Loading...</div>;
  } else {
    return (
      <div className="App">
        <h1>Pokemons</h1>
        <div className="wrap">
          <div className="search">
            <input type="text" className="searchTerm" placeholder="Search..." onChange={(event) => setSearch(event.target.value)}  />
          </div>
          <div className="search">
            <select className="searchTerm" value={filterBy} onChange={(event) => {setFilterBy(event.target.value)}}>
              <option value="">Select value</option>
              <option value="base_experience">Base Experience</option>
              <option value="height">Height</option>
              <option value="weight">Weight</option>
            </select>
          </div>
          <div className="search">
            <input type="text" className="searchTerm" placeholder="Enter filter value" onChange={(event) => setFilterValue(event.target.value)}  />
          </div>
          <button type="submit" className="searchButton" onClick={filterData}>
              Search
          </button>
        </div>
        <DataTable
          columns={columns}
          data={items}
          pagination
          paginationServer
          paginationTotalRows={totalRows}
          onChangePage={handlePageChange}
          onChangeRowsPerPage={handlePerRowsChange}
        />
      </div>
    );
  }
}

export default App;
