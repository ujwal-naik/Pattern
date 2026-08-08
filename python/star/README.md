# Star Pattern Scripts

This folder contains Python scripts to draw ASCII star shapes in the terminal.

## Files

- `star.py` - draws a solid 5-point star using a filled polygon render.
- `hollow_star.py` - draws a hollow 5-point star using connected outline segments.

## Requirements

- Python 3

## Usage

From the `python/star` directory, run:

```bash
python star.py
```

or:

```bash
python hollow_star.py
```

## Sample Output

### `star.py`

```text
                                                            *
                                                            *
                                                            *
                                                           ***
                                                           ***
                                                          *****
                                                          *****
                                                         *******
                                                         *******
                                                        *********
                                                        *********
                                                       ***********
                                                       ***********
                                    *************************************************
                                      *********************************************
                                        *****************************************
                                          *************************************
                                            *********************************
                                              *****************************
                                                *************************
                                                  *********************
                                                   *******************
                                                  *********************
                                                  *********************
                                                  *********************
                                                 ***********************
                                                 *********** ***********
                                                **********     **********
                                                ********         ********
                                               *******             *******
                                               *****                 *****
                                              ****                     ****
                                              **                         **
                                             *                             *
```

### `hollow_star.py`

```text
                                                            *
                                                            *
                                                           * *
                                                           * *
                                                          *   *
                                                          *   *
                                                         *     *
                                                         *     *
                                                        *       *
                                                        *       *
                                                       *         *
                                                       *         *
                                                      *          *
                                   **************************************************
                                    **               *            *              **
                                      **             *             *           **
                                        **          *              *         **
                                          **        *               *      **
                                            **     *                *    **
                                              **   *                 * **
                                                ***                  **
                                                  **               ** *
                                                 *  **           **   *
                                                 *    **       **     *
                                                *       **   **        *
                                                *         ***          *
                                               *         ** **          *
                                               *       **     **        *
                                              *      **         **       *
                                              *    **             **     *
                                             *   **                 **    *
                                             * **                     **  *
                                            ***                         ** *
                                            *                             **
```

## Notes

- The output is optimized for monospaced terminal fonts.
- Adjust `width`, `height`, and `x_scale` in the scripts if the star looks stretched in your terminal.
