import axios from 'axios';

const instance = axios.create({
    withCredentials: true,
    baseURL: '',
    headers: {
        "API-KEY": "612b1c54-63ba-43f8-93bb-fa6787606cc9"
    },
});

export const usersAPI = {
    getUsers(currentPage = 1, pageSize = 10) {
        return instance.get(`users?page=${currentPage}&count=${pageSize}`)
          .then(response => {
            return response.data;
          });
    },
    follow(userId) {
        return instance.post(`follow/${userId}`)
    },
    unfollow(userId) {
        return instance.delete(`follow/${userId}`)
    },
    getProfile(userId) {
        console.warn('Obsolete method. Please profileAPI object.')
        return profileAPI.getProfile(userId)
    }
}

export const profileAPI = {
    getProfile(userId) {
        return instance.get(`profile/` + userId);
    },
    getStatus(userId) {
        return instance.get(`profile/status/` + userId);
    },
    updateStatus(status) {
        return instance.put(`profile/status`, { status: status });
    }
   }

export const authAPI = {
   me() {
    return instance.get(`auth/me`);
   }
}
