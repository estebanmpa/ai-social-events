import { CONFIG } from "@/global-config";
import axios from "axios";

export const axiosInstance = () => {
    const instance = axios.create({
        baseURL: CONFIG.apiBaseUrl,
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    });

    return instance;
}
