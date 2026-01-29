const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

export const checkBackendStatus = async () => {
    try {
        const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error checking backend status:', error);
        throw error;
    }
};

export const getUsers = async () => {
    try {
        const response = await fetch(`${API_URL}/users`);
        if (!response.ok) throw new Error('Failed to fetch users');
        return await response.json();
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};

export const getUser = async (userId) => {
    try {
        const response = await fetch(`${API_URL}/users/${userId}`);
        if (!response.ok) throw new Error('User not found');
        return await response.json();
    } catch (error) {
        console.error('Error fetching user:', error);
        throw error;
    }
};

export const createUser = async (userData) => {
    try {
        const response = await fetch(`${API_URL}/users`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
        });
        if (!response.ok) throw new Error('Failed to create user');
        return await response.json();
    } catch (error) {
        console.error('Error creating user:', error);
        throw error;
    }
}; 