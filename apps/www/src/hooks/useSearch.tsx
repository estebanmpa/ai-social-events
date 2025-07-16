import { useEffect, useState } from 'react'
import { axiosInstance } from '@/utils/axios-instance'

type StateType = {
  data: any[],
  loading: boolean,
  error: boolean
}

const initialState: StateType = {
  data: [],
  loading: true,
  error: false
}

export default function useSearch() {
  const [state, setState] = useState(initialState)

  const fetchData = async (query: string) => {
    try {
      setState((prevState) => ({ ...prevState, loading: true, error: false }))
      const results = await axiosInstance().get('/search/', {
        params: {
          q: encodeURIComponent(query)
        }
      })
      setState((prevState) => ({ ...prevState, loading: false, data: results.data?.items }))
    } catch (error) {
      setState((prevState) => ({ ...prevState, loading: false, error: true }))
    }
  }

  return { ...state, fetchData }
}
