from typing import List

import sys
from sympy import Point2D

from datasets.Rectangle import Rectangle


class Symbol:
    def __init__(self, content: str, strokes: List[List[Point2D]], symbol_name: str, dimensions: Rectangle) -> None:
        super().__init__()
        self.dimensions = dimensions
        self.symbol_name = symbol_name
        self.content = content
        self.strokes = strokes

    @staticmethod
    def initialize_from_string(content: str) -> 'Symbol':
        """
        Create and initializes a new symbol from a string
        :param content: The content of a symbol as read from the text-file
        :return: The initialized symbol
        :rtype: Symbol
        """

        if content is None or content is "":
            return None

        lines = content.splitlines()
        min_x = sys.maxsize
        max_x = 0
        min_y = sys.maxsize
        max_y = 0

        symbol_name = lines[0]
        strokes = []
        dimensions = Rectangle(Point2D(min_x, min_y), max_x - min_x + 1, max_y - min_y + 1)

        return Symbol(content, strokes, symbol_name, dimensions)

    #
    #     public static Symbol InitializeFromString(string content)
    #     {
    #         var lines = content.Split(new[] { "\n", "\r\n" }, StringSplitOptions.None);
    #
    #         var newSymbol = new Symbol
    #         {
    #             FileContent = content,
    #             SymbolName = lines[0]
    #         };
    #
    #         int minX = int.MaxValue;
    #         int maxX = 0;
    #         int minY = int.MaxValue;
    #         int maxY = 0;
    #
    #         foreach (var strokeString in lines.Skip(1))
    #         {
    #             var stroke = new List<Point>();
    #             foreach (var pointString in strokeString.Split(';').Where(s => s != "")) // Each stroke ends with a ; so the last element after the split should be skipped
    #             {
    #                  var point = new Point(int.Parse(pointString.Split(',')[0]), int.Parse(pointString.Split(',')[1]));
    #                  stroke.Add(point);
    #
    #                  maxX = Math.Max(maxX, point.X);
    #                  minX = Math.Min(minX, point.X);
    #                  maxY = Math.Max(maxY, point.Y);
    #                  minY = Math.Min(minY, point.Y);
    #             }
    #
    #             newSymbol.Strokes.Add(stroke);
    #             newSymbol.Dimensions = new Rectangle(minX, minY, maxX - minX + 1, maxY - minY + 1);
    #         }
    #
    #         return newSymbol;
    #     }
    #




    def draw_into_bitmap(self, export_file_name: str, stroke_thickness: int, margin: int = 2):
        pass

    #     /// <summary>
    #     ///
    #     /// </summary>
    #     /// <param name="exportFileName"></param>
    #     /// <param name="strokeThickness"></param>
    #     /// <param name="margin">Additional margin, especially useful, if strokeThickness is bigger than one, to prevent drawing outside of image</param>
    #     public Size DrawIntoBitmap(string exportFileName, int strokeThickness, int margin = 2)
    #     {
    #          var width = Dimensions.Width + 2*margin;
    #          var height = Dimensions.Height + 2*margin;
    #          var offset = new Point(Dimensions.Location.X - margin, Dimensions.Location.Y - margin);
    #
    #          using (var bmp = new Bitmap(width, height))
    #          {
    #              using (Graphics g = Graphics.FromImage(bmp))
    #              {
    #                   g.FillRectangle(new SolidBrush(Color.White), 0, 0, width, height);
    #                   foreach (var stroke in Strokes)
    #                   {
    #                       for (int i = 0; i < stroke.Count - 1; i++)
    #                       {
    #                           var startPoint = SubtractOffset(stroke[i], offset);
    #                           var endPoint = SubtractOffset(stroke[i + 1], offset);
    #                           g.DrawLine(new Pen(Color.Black, strokeThickness), startPoint, endPoint);
    #                       }
    #                   }
    #
    #                   bmp.Save(exportFileName, ImageFormat.Png);
    #               }
    #          }
    #
    #          return new Size(width, height);
    #     }
    #



    def draw_into_bitmap(self, export_file_name: str, stroke_thickness: int, margin: int, destination_width: int,
                         destination_height: int):
        pass

# public Size DrawIntoBitmap(string exportFileName, int strokeThickness, int margin, int destinationWidth, int destinationHeight)
# {
# var width = Dimensions.Width + 2*margin;
# var height = Dimensions.Height + 2*margin;
# var widthOffsetForCentering = (destinationWidth - width) / 2;
# var heightOffsetForCentering = (destinationHeight - height) / 2;
# var offset = new Point(Dimensions.Location.X - margin - widthOffsetForCentering, Dimensions.Location.Y - margin - heightOffsetForCentering);
#
# using (var bmp = new Bitmap(destinationWidth, destinationHeight))
# {
#     using (Graphics g = Graphics.FromImage(bmp))
# {
#     g.FillRectangle(new SolidBrush(Color.White), 0, 0, destinationWidth, destinationHeight);
# foreach (var stroke in Strokes)
# {
# for (int i = 0; i < stroke.Count - 1; i++)
# {
# var startPoint = SubtractOffset(stroke[i], offset);
# var endPoint = SubtractOffset(stroke[i + 1], offset);
# g.DrawLine(new Pen(Color.Black, strokeThickness), startPoint, endPoint);
# }
# }
#
# bmp.Save(exportFileName, ImageFormat.Png);
# }
# }
#
# return new Size(width, height);
# }
#
#
#
#
#     def SubtractOffset(Point a, Point b) -> Point:
#         return new Point(a.X - b.X, a.Y - b.Y);
#