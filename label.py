import pandas as pd
import os

# 1: active, 0: fatigue

def labeling(dirpath, mode):
    df = pd.DataFrame(columns=["path", "label"])
    for dir, _, files in os.walk(dirpath):
        for file in files:
            img_path = os.path.relpath(os.path.join(dir, file), start="data\FERPlus")
            if "active" in img_path:
                label = 1
            elif "fatigue" in img_path:
                label = 0
            df.loc[len(df.index)] = [img_path, label]
    df.to_csv(f"data\\FERPlus\\{mode}.csv", index=False)

if __name__ == "__main__":
    labeling("data\\FERPlus\\images\\train", mode="train")
    labeling("data\\FERPlus\\images\\test", mode="test")