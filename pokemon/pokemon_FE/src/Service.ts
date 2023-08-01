import Axios from "axios";

export async function getData(page: number, perPage: number, keyword?: string, filterBy?: string, filterValue?: string): Promise<any> {
    try {
    const response = await Axios.get(
    "http://localhost:8000/pokemons", {
        params: {page: page, per_page: perPage, keyword: keyword, filter_by: filterBy, filter_value: filterValue}
    }
    );
    return response.data;
    } catch(error) {
        throw error;
    }
}
