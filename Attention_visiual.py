import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(3, 3, sharex=True, sharey=True, figsize=(6, 6))
fig.subplots_adjust(wspace=0, hspace=0.1)

for i, row in enumerate(axes):
    for j, col in enumerate(row):
        im = col.imshow(np.arange(100).reshape((10, 10)))
        #         ax_cb = fig.colorbar(im, ax=col)
        if col.is_last_row():
            col.set_xlabel('x')
        if col.is_first_col():
            col.set_ylabel('y')

cb = fig.colorbar(im, ax=axes.ravel().tolist(), orientation='horizontal')
cb.ax.tick_params()
cb.set_label("colorbar")

# plt.tight_layout() # 使用 tight layout 需要手动调整 colorbar 位置，否则会很难看
plt.show()
