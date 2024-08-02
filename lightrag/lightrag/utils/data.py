import numpy as np
from abc import ABC, abstractmethod


class Dataset(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __getitem__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass


class DataLoader:
    __doc__ = r"""A simplified version of PyTorch DataLoader.

    The biggest difference is not to handle tensors, but to handle any type of data."""

    def __init__(self, dataset, batch_size: int = 4, shuffle: bool = True):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.indices = np.arange(len(dataset))
        self.current_index = 0

    def __iter__(self):
        if self.shuffle:
            np.random.shuffle(self.indices)
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.dataset):
            raise StopIteration

        batch_indices = self.indices[
            self.current_index : self.current_index + self.batch_size
        ]
        batch_data = [self.data[int(i)] for i in batch_indices]

        if isinstance(batch_data[0], tuple):
            batch_data = tuple(zip(*batch_data))
        else:
            batch_data = np.array(batch_data)

        self.current_index += self.batch_size

        return batch_data
