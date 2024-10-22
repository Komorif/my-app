"use client";

import React, { useEffect, useState } from 'react';

// Подключение css
import styles from './video.module.css'

interface AnimeVideo {
  image: string;
  title: string;
  genre: string;
  date: number;
  month: string;
  description: string;
}


const AnimeVideoComponent: React.FC = () => {
  const [animeVideos, setAnimeVideos] = useState<AnimeVideo[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Функция для получения данных с API
  const fetchAnimeVideos = async () => {
    try {
      const response = await fetch('http://localhost:8000', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      
      if (!response.ok) {
        throw new Error('Ошибка при получении данных');
      }

      const data: AnimeVideo[] = await response.json();
      setAnimeVideos(data);
      setLoading(false);
    } catch (err) {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAnimeVideos();
  }, []);

  if (loading) {
    return <p>Загрузка...</p>;
  }

  if (error) {
    return <p>Ошибка: {error}</p>;
  }

  return (
    <div>
      
      <div className={styles.header}>
        <a href="#default" className={styles.logo}>AniFlix</a>
        <div className={styles.header_right}>
          <a className={styles.active} href="@">Главная</a>
          <a href="#contact">Контакты</a>
          <a href="#about">О нас</a>
        </div>
      </div>

      <div className={styles.videos}>
        <ul>
          {animeVideos.map((video, index) => (
            <li key={1} className={styles.product_wrapper}>
              {video.image && <img src={video.image} alt={video.title} width="100" height="150"/>}
              <p>{video.title}</p>
              <p>{video.genre}</p>
              <p>{video.date}</p>
              <p>{video.month}</p>
              <p>{video.description}</p>
            </li>
          ))}
        </ul>
      </div>
      



    </div>
  );
};

export default AnimeVideoComponent;