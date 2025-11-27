export enum UserRole {
  VOLUNTEER = 'VOLUNTEER',
  ADMIN = 'ADMIN'
}

export enum ActivityCategory {
  ENVIRONMENT = 'Environment',
  EDUCATION = 'Education',
  ELDERLY_CARE = 'Elderly Care',
  ANIMAL_WELFARE = 'Animal Welfare',
  COMMUNITY = 'Community',
  HEALTH = 'Health'
}

export enum ActivityStatus {
  OPEN = 'Open',
  FULL = 'Full',
  COMPLETED = 'Completed',
  CANCELLED = 'Cancelled'
}

export interface User {
  id: string;
  name: string;
  email: string;
  role: UserRole;
  avatar?: string;
  phone?: string;
  totalHours: number;
  eventsJoined: number;
}

export interface Activity {
  id: string;
  title: string;
  description: string;
  date: string;
  time: string;
  location: string;
  category: ActivityCategory;
  image: string;
  capacity: number;
  registeredCount: number;
  status: ActivityStatus;
  organizer: string;
}

export interface Registration {
  id: string;
  activityId: string;
  userId: string;
  registrationDate: string;
  status: 'REGISTERED' | 'CHECKED_IN' | 'CANCELLED';
  checkInTime?: string;
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
}