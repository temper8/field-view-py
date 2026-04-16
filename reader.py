import h5py
import numpy as np

def dataset_reader(file_path, dataset_name):
    try:
        # Открываем файл в режиме чтения
        with h5py.File(file_path, 'r') as f:
            # Проверяем существование набора данных
            if dataset_name not in f:
                raise ValueError(f"Набор данных '{dataset_name}' не найден в файле")
            
            dataset = f[dataset_name]
                      
            # Выводим информацию о массиве
            print(f"Успешно прочитан массив: {dataset_name}")
            print(f"Размерность: {dataset.shape}")
            print(f"Тип данных: {dataset.dtype}")
            
            # Читаем весь массив в память (осторожно с большими данными!)
            return np.array(dataset)

    except Exception as e:
        print(f"Ошибка: {str(e)}")
        exit(1)

if __name__ == '__main__':
    # Укажите путь к вашему HDF5 файлу
    file_path = 'data/results.h5'
                                   # Имя 2D массива внутри HDF5-файла
    X =  dataset_reader(file_path, '/nphi-122/grid_2d/X')
    Y =  dataset_reader(file_path, '/nphi-122/grid_2d/Y')
    Ea = dataset_reader(file_path, '/nphi-122/field_2d/Ea')

    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    im1 = ax1.pcolormesh(X, Y, Ea[:,:], shading='gouraud', cmap="plasma",)
    fig.colorbar(im1, ax=ax1)
    ax1.set_aspect('equal')
    ax1.set_title('Ea')
    im2 = ax2.pcolormesh(X, Y, Ea[:,:], norm=LogNorm(vmin=Ea.min(), vmax=Ea.max()), shading='gouraud', cmap="plasma",)
    fig.colorbar(im2, ax=ax2)
    ax2.set_aspect('equal')
    ax2.set_title('Ea (LogNorm)')
    fig.savefig('double_disk.png')  
    plt.show()
