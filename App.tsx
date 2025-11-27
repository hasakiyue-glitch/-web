import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import { Layout } from './components/Layout';
import { Home } from './pages/Home';
import { ActivityDetail } from './pages/ActivityDetail';
import { Auth } from './pages/Auth';
import { Profile } from './pages/Profile';
import { CheckIn } from './pages/CheckIn';
import { Admin } from './pages/Admin';
import { StoreProvider } from './contexts/StoreContext';

const App = () => {
  return (
    <StoreProvider>
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/activity/:id" element={<ActivityDetail />} />
            <Route path="/auth" element={<Auth />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/checkin" element={<CheckIn />} />
            <Route path="/admin" element={<Admin />} />
          </Routes>
        </Layout>
      </Router>
    </StoreProvider>
  );
};

export default App;