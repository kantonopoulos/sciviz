import unittest
import pandas as pd
import seaborn as sns
from sciviz.src.palettes import color_seq_palette, shape_palette, size_palette, set_palettes, set_order

class TestPaletteUtils(unittest.TestCase):

    def test_default_color(self):
        palette = [(0.13333333333333333, 0.44313725490196076, 0.7098039215686275), 
                   (0.8627450980392157, 0.0, 0.0)]
        test_df = pd.DataFrame({'color': ['A', 'B', 'A', 'A', 'B']})
        pal_default = color_seq_palette(test_df['color'])
        self.assertEqual(pal_default, palette)
    
    def test_default_more_than_10_color(self):
        palette = sns.color_palette('deep')
        test_df = pd.DataFrame({'color': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']})
        pal_default = color_seq_palette(test_df['color'])
        self.assertEqual(pal_default, palette[:len(test_df['color'].unique())])

    def test_user_specified_color(self):
        palette = [(0.6196078431372549, 0.00392156862745098, 0.25882352941176473), 
                   (0.3215686274509804, 0.5411764705882353, 0.38823529411764707)]
        test_df = pd.DataFrame({'color': ['A', 'B', 'A', 'A', 'B']})
        pal_user_specified = color_seq_palette(test_df['color'], users_palette = ['#9E0142', '#528A63'])
        self.assertEqual(pal_user_specified, palette)

    def test_user_specified_cycled_color(self):
        palette = [(0.6196078431372549, 0.00392156862745098, 0.25882352941176473)]*2
        test_df = pd.DataFrame({'color': ['A', 'B', 'A', 'A', 'B']})
        pal_user_specified = color_seq_palette(test_df['color'], users_palette = ['#9E0142'])
        self.assertEqual(pal_user_specified, palette)

    def test_default_shape(self):
        palette = ['o', 's']
        test_df = pd.DataFrame({'shape': ['A', 'B', 'A', 'A', 'B']})
        pal_default = shape_palette(test_df['shape'])
        self.assertEqual(pal_default, palette)  

    def test_user_specified_shape(self):
        palette = ['^', 'X']
        test_df = pd.DataFrame({'shape': ['A', 'B', 'A', 'A', 'B']})
        pal_user_specified = shape_palette(test_df['shape'], users_palette = ['^', 'X'])
        self.assertEqual(pal_user_specified, palette)

    def test_default_size(self):
        palette = {'A': 50, 'B': 100}
        test_df = pd.DataFrame({'size': ['A', 'B', 'A', 'A', 'B']})
        pal_default = size_palette(test_df['size'], 50, 100)
        self.assertEqual(pal_default, palette)  
    
    def test_set_palettes(self):
        test_df = pd.DataFrame({'color': ['A', 'B', 'A', 'A', 'B'], 
                                'shape': ['C', 'D', 'C', 'C', 'C'], 
                                'size': ['E', 'E', 'E', 'F', 'F']})
        size_limits=[50, 100]
        color_pal, shape_pal, size_pal, size_num = set_palettes(test_df, 'color', 'shape', 'size', 
                                                                color_pal=None, shape_pal=None, size_pal=size_limits)
        fun_output = [color_pal, shape_pal, size_pal, size_num]
        expected_output = [color_seq_palette(test_df['color']), shape_palette(test_df['shape']), 
                           size_palette(test_df['size'], size_limits[0], size_limits[1]), False]  
        self.assertEqual(fun_output, expected_output)

    def test_set_palettes_color_int_size(self):
        test_df = pd.DataFrame({'color': ['A', 'B', 'A', 'A', 'B']})
        size = 50
        color_pal, shape_pal, size_pal, size_num = set_palettes(test_df, 'color', shape=None, size=size, 
                                                                color_pal=None, shape_pal=None, size_pal=None)
        fun_output = [color_pal, shape_pal, size_pal, size_num]
        expected_output = [color_seq_palette(test_df['color']), None, None, True]
        self.assertEqual(fun_output, expected_output)
    
    def test_set_palettes_shape_no_size(self):
        test_df = pd.DataFrame({'shape': ['A', 'B', 'A', 'A', 'B']})
        color_pal, shape_pal, size_pal, size_num = set_palettes(test_df, color=None, shape='shape', size=None, 
                                                                color_pal=None, shape_pal=None, size_pal=None)
        fun_output = [color_pal, shape_pal, size_pal, size_num]
        expected_output = [None, shape_palette(test_df['shape']), None, False]
        self.assertEqual(fun_output, expected_output)

    def test_set_palettes_int_size(self):
        test_df = pd.DataFrame({'color': ['A', 'B', 'A', 'A', 'B']})
        size = 50
        color_pal, shape_pal, size_pal, size_num = set_palettes(test_df, color=None, shape=None, size=size, 
                                                                color_pal=None, shape_pal=None, size_pal=None)
        fun_output = [color_pal, shape_pal, size_pal, size_num]
        expected_output = [None, None, None, True]
        self.assertEqual(fun_output, expected_output)

    def test_set_order(self):
        test_df = pd.DataFrame({'color': ['A', 'B', 'A', 'A', 'B'], 
                                'shape': ['C', 'D', 'C', 'C', 'C'], 
                                'size': ['E', 'E', 'E', 'F', 'F']})
        # Prioritize color, then shape, then size if conflict exists
        color_order, shape_order, size_order = set_order('color', ['B', 'A'], 
                                                         'color', None, 
                                                         'size', ['E', 'F'])
        fun_output = [color_order, shape_order, size_order]
        expected_output = [['B', 'A'], ['B', 'A'], ['E', 'F']]
        self.assertEqual(fun_output, expected_output)


if __name__ == '__main__':
    unittest.main()